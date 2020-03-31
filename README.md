# 1082_Embedded-Image-Processing_HW1

作業1 : opencv 與AVX </p>

把一張影像做灰階化後做threasholding，門檻值為128，大於128為255，小於或等於128為0。 </p>

接著做morphology裡面的open和close，各做100次，kernel要為3*3到9*9之間，紀錄做open和close的執行速度。 </p>

比對以下項目的差別： </p>

1.沒有使用AVX </p>

2.使用AVX </p>

3.查multi thread(map & reduce)加速 </p>


# 結果 </p>
- 硬體設備: </p>
CPU: AMD 3500X </p>
RAM: DDR4 16G </p>
- 執行環境: </p>
OS: WIN 10 </p>
Python version : 3.7 </p>
Opencv version : 3.4.1 </p>

- Opening </p>
使用AVX優化後執行100次opening，執行時間為1269ms。</p>
使用AVX優化後執行100次opening，執行時間為1.412s。</p>
(由於只關閉AVX需修改CMake內容，且須使用c++，整體較為複雜，此處改為呼叫cv2.setUseOptimized 關閉所有優化，包含SSE2,AVX..等)</p>
Speedup : 11.1247 </p>


- Closing </p>
使用AVX優化後執行100次closing，執行時間為1265ms。</p>
使用AVX優化後執行100次closing，執行時間為1.412s。</p>
(由於只關閉AVX需修改CMake內容，且須使用c++，整體較為複雜，此處改為呼叫cv2.setUseOptimized 關閉所有優化，包含SSE2,AVX..等)</p>
Speedup : 11.1611 </p>

