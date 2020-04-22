### System Engineer (SRE) Study Notes

- [CAP Theory](https://en.wikipedia.org/wiki/CAP_theorem)
  - Extensions:
    - [CAP Twelve Years Later: How the "Rules" Have Changed ](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
    - [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html)
    - [1Replicated Data Consistency Explained Through Baseball](https://www.microsoft.com/en-us/research/wp-content/uploads/2011/10/ConsistencyAndBaseballReport.pdf)


- Databases
  - [mongo](https://aphyr.com/posts/322-call-me-maybe-mongodb-stale-reads)
  - [aws dynamodb](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)


- Streams
  - **Kafka**  
    [Kafka White Paper](http://notes.stephenholiday.com/Kafka.pdf)
    - **Caching**

       Kafka uses page cache instead of in memory cache, thus the overhead of GC is low, see links below for details of page cache, and it has the   benefit  of  retaining warm cache even when a broker process is restarted
      - [Page Cache](https://en.wikipedia.org/wiki/Page_cache)
      - [Page Cache, the Affair Between Memory and Files](https://manybutfinite.com/post/page-cache-the-affair-between-memory-and-files/)
    - **File Copying**
       A typical  approach  to  sending  bytes  from  a  local  file  to  a  remote socket involves the following steps:
          (1) read data from the storage media to the page cache in an OS
          (2) copy data in the page cache to  an  application  buffer  
          (3) copy  application  buffer  to  another kernel  buffer  
          (4) send  the  kernel  buffer  to  the  socket.  
        This includes  4  data  copying  and  2  system  calls.  On  Linux  and  other Unix  operating  systems,  there  exists  a  sendfile  API  [5]  that  can directly  transfer  bytes  from  a  file  channel  to  a  socket  channel. This typically avoids 2 of the copies and 1 system call introduced in steps (2) and (3). Kafka exploits the sendfile API to efficiently deliver bytes in a log segment file from a broker to a consumer.
       - [send file API](http://man7.org/linux/man-pages/man2/sendfile.2.html)
       - [FD debug](https://www.codelast.com/%E5%8E%9F%E5%88%9B-%E8%A7%A3%E5%86%B3linux%E7%B3%BB%E7%BB%9F%E4%B8%8A%E7%94%B1%E4%BA%8E%E7%A8%8B%E5%BA%8F%E5%8D%A0%E7%94%A8%E7%9A%84%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6file-descriptor/)
       - [FD debug](https://segmentfault.com/a/1190000009724931)
       - [Zero Copy I: User-Mode Perspective ](https://www.linuxjournal.com/article/6345)

- Linux:
  - [File Descriptor: S.Chinese](https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/linux-jin-cheng)

- Cache
  - Read Through
  - Write Through
  - Write back

  - Reading list
    - [Facebook’sDistributedDataStorefortheSocialGraph](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)
