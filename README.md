# 1082_Embedded-Image-Processing_HW1

作業1 : opencv 與AVX </p>

把一張影像做灰階化後做threasholding，門檻值為128，大於128為255，小於或等於128為0。 </p>

接著做morphology裡面的open和close，各做100次，kernel要為3*3到9*9之間，紀錄做open和close的執行速度。 </p>

比對以下項目的差別： </p>

1.沒有使用AVX </p>

2.使用AVX </p>

3.查multi thread(map & reduce)加速 </p>


# 結果 </p>
- 硬體設備 </p>
CPU: AMD 3500X </p>
RAM: DDR4 16G </p>
- 執行環境 </p>
OS: WIN 10 </p>
Python version : 3.7 </p>
Opencv version : 3.4.1 </p>

- 原始影像</p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW1/blob/master/imagetest/photo.jpeg)

- 二質化 </p>
以128為分界，大於128為255，小於等於128為0 </p>
執行結果</p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW1/blob/master/imagetest/Binarization.jpeg)

- Opening </p>
kernel為3x3</p>
使用AVX優化後執行100次opening，執行時間為1611ms。</p>
關閉AVX優化後執行100次opening，執行時間為1.494s。</p>
(由於只關閉AVX需修改CMake內容，且須使用c++，整體較為複雜，此處改為呼叫cv2.setUseOptimized 關閉所有優化，包含SSE2,AVX..等)</p>
Speedup : 9.27 </p>
執行結果</p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW1/blob/master/imagetest/opening_with_avx.jpeg)

- Closing </p>
kernel為3x3</p>
使用AVX優化後執行100次closing，執行時間為1604ms。</p>
關閉AVX優化後執行100次closing，執行時間為1.5s。</p>
(由於只關閉AVX需修改CMake內容，且須使用c++，整體較為複雜，此處改為呼叫cv2.setUseOptimized 關閉所有優化，包含SSE2,AVX..等)</p>
Speedup : 9.35 </p>
執行結果</p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW1/blob/master/imagetest/closing_whit_avx.jpeg)

</r>
</r>

# Multi thread and Mapreduce </p>
- Multi thread  </p>
multithreading 是一種以重疊的方式讓單顆 CPU 內多個 threads 以能夠共用功能單元，與 multiprocessor 的差別在於， multithreading 不須複製多個processors ，而是讓 threads 之間共用 CPU 的大多功能，複製的只有 threads 各自的狀態，像是 regester,program counter...等等。  </p>

而在影像處理的領域中，使用 multithreading 的技術可以提升整體運算的效率，像是在 I/O 讀取中的空檔，又或是 memory failure 的空檔中，插入另一個 thread 來執行，使得空閒中的 CPU 有事情做，可讓整體 throughtput 增加。  </p>

- Mapreduce  </p>
Mapreduce 是由 Google 在2003年所提出的函式庫，首先將要執行的問題，拆解成 Map 和 Reduce 的方式來執行(類似於 divide and conquer)，以達到分散運算的效果。 </p>
步驟為: </p>
1.將要執行的 MapReduce 程式複製到 Master 與每一臺 Worker 機器中。 </p>
2.Master 決定 Map 程式與 Reduce 程式，分別由哪些 Worker 機器執行。 </p>
3.將所有的資料區塊，分配到執行 Map 程式的 Worker 機器中進行 Map。 </p>
4.將 Map 後的結果存入 Worker 機器的本地磁碟。 </p>
5.執行 Reduce 程式的 Worker 機器，遠端讀取每一份 Map 結果，進行彙整與排序，同時執行 Reduce 程式。 </p>
6.將使用者需要的運算結果輸出。 </p>


- 參考資料: </p>
computer architecture a quantitative approach 6th </p>
[Mapreduce](https://blog.alantsai.net/posts/2017/12/data-science-series-09-hadoop-map-reduce-java-wordcount-example) </p>
[hadoop](https://www.inside.com.tw/article/4428-big-data-4-hadoop) </p>



