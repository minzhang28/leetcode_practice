## Network


#### [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
Shortcuts:
- TCP segment header
  - Source port (16 bits)
    Identifies the sending port.
  - Destination port (16 bits)
    Identifies the receiving port.
  - Sequence number (32 bits)
     - Has a dual role:
        - If the SYN flag is set (1), then this is the initial sequence number. The sequence number of the actual first data byte and the acknowledged number in the corresponding ACK are then this sequence number plus 1.
        - If the SYN flag is clear (0), then this is the accumulated sequence number of the first data byte of this segment for the current session.

  - Acknowledgment number (32 bits)
     - If the ACK flag is set then the value of this field is the next sequence number that the sender of the ACK is expecting. This acknowledges receipt of all prior bytes (if any). The first ACK sent by each end acknowledges the other end's initial sequence number itself, but no data.
  - Flags (9 bits)
       Contains 9 1-bit flags (control bits) as follows:

        - NS (1 bit): ECN-nonce - concealment protection[a]
        - CWR (1 bit): Congestion window reduced (CWR) flag is set by the sending host to indicate that it received a TCP segment with the ECE flag set and had responded in congestion control mechanism.[b]
        - ECE (1 bit): ECN-Echo has a dual role, depending on the value of the SYN flag. It indicates:
            - If the SYN flag is set (1), that the TCP peer is ECN capable.
            - If the SYN flag is clear (0), that a packet with Congestion Experienced flag set (ECN=11) in the IP header was received during normal transmission.[b] This serves as an indication of network congestion (or impending congestion) to the TCP sender.
        - URG (1 bit): Indicates that the Urgent pointer field is significant
        - ACK (1 bit): Indicates that the Acknowledgment field is significant. All packets after the initial SYN packet sent by the client should have this flag set.
        - PSH (1 bit): Push function. Asks to push the buffered data to the receiving application.
        - RST (1 bit): Reset the connection
        - SYN (1 bit): Synchronize sequence numbers. Only the first packet sent from each end should have this flag set. Some other flags and fields change meaning based on this flag, and some are only valid when it is set, and others when it is clear.
        - FIN (1 bit): Last packet from sender