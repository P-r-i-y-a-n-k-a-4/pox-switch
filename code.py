from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    dpid = event.connection.dpid
    mac_to_port.setdefault(dpid, {})

    # Learn source MAC
    mac_to_port[dpid][packet.src] = event.port

    # If destination known → forward
    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]

        # Install flow rule
        fm = of.ofp_flow_mod()
        fm.match = of.ofp_match.from_packet(packet)
        fm.idle_timeout = 10
        fm.hard_timeout = 30
        fm.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(fm)

        # Send current packet
        po = of.ofp_packet_out()
        po.data = event.ofp
        po.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(po)

        log.info("Forward %s -> %s via %s",
                 packet.src, packet.dst, out_port)

    else:
        # FLOOD (important for ARP)
        po = of.ofp_packet_out()
        po.data = event.ofp
        po.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(po)

        log.info("Flooding %s", packet.src)


def launch():
    log.info("Custom Controller Running...")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)