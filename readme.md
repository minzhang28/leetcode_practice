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

        -  read data from the storage media to the page cache in an OS
        -  copy data in the page cache to  an  application  buffer  
        -  copy  application  buffer  to  another kernel  buffer  
        -  send  the  kernel  buffer  to  the  socket.  

        This includes  4  data  copying  and  2  system  calls.  On  Linux  and  other Unix  operating  systems,  there  exists  a  sendfile  API  [5]  that  can directly  transfer  bytes  from  a  file  channel  to  a  socket  channel. This typically avoids 2 of the copies and 1 system call introduced in steps (2) and (3). Kafka exploits the sendfile API to efficiently deliver bytes in a log segment file from a broker to a consumer.
       - [send file API](http://man7.org/linux/man-pages/man2/sendfile.2.html)
       - [FD debug](https://segmentfault.com/a/1190000009724931)
       - [Zero Copy I: User-Mode Perspective ](https://www.linuxjournal.com/article/6345)

- Linux:
  - [File Descriptor: S.Chinese](https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/linux-jin-cheng)

- Cache

  - Write through cache : This is a caching system where writes go through the cache and write is confirmed as success only if writes to DB and the cache BOTH succeed. This is really useful for applications which write and re-read the information quickly. However, write latency will be higher in this case as there are writes to 2 separate systems.
  - Write around cache : This is a caching system where write directly goes to the DB. The cache system reads the information from DB incase of a miss. While this ensures lower write load to the cache and faster writes, this can lead to higher read latency incase of applications which write and re-read the information quickly.
  - Write back cache : This is a caching system where the write is directly done to the caching layer and the write is confirmed as soon as the write to the cache completes. The cache then asynchronously syncs this write to the DB. This would lead to a really quick write latency and high write throughput. But, as is the case with any non-persistent / in-memory write, we stand the risk of losing the data incase the caching layer dies. We can improve our odds by introducing having more than one replica acknowledging the write ( so that we don’t lose data if just one of the replica dies ).
  - LRU
    - [leetcode question](https://leetcode.com/problems/lru-cache/)
  - LFU
    - [leetcode question](https://leetcode.com/problems/lfu-cache/)
    - [LFU white paper](http://dhruvbird.com/lfu.pdf)

  - Reading list
    - [Facebook’s Distributed DataStore for the Social Graph](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)
