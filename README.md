###### python mid exam
# D. Production

<object data="./d.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="./d.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="./d.pdf">Download PDF</a>.</p>
    </embed>
</object>


<center> 出題者 : ニオ </center>
<center> Time : 4s </center>
<center> Memory : 512MiB </center>
</br>

<center>
<img src="https://i.imgur.com/ZtaQOVc.png" width=330>
<br>
<font size="1" color="909090">阿斯托爾福:在輕小說《Fate/Apocrypha》中初次登場</font>
</center>
<br>

**僕は君の剣！**  
直譯來說就是:我就是你的劍！  
每個可愛的男孩子都該有一把短劍  
為了使短劍配率上升，可愛的阿福決定開一間自動鐵匠鋪  
因為是第一次嘗試，笨笨阿福不知道要先開幾條生產線  
但是客人至上，品質總要是最好的吧 !! 因此多條生產線的最終產品只會選擇品質較高者來出售  
是這樣的，每條生產線上會有五台檢測機，其功能分別為產出下列描述:  

---
**A** 
> 敲打煉鐵，練度增加 ( $p+q$ )

**B**
> 過度用力，練度減少 ( $p-q$ )

**C**
> 加熱加工，練度加乘 ( $p \times q$ )

**D**
> 太熱融化，練度除以 ( $p \div q$ )

**E**
> 機器過熱，生產線無條件停止，不再生產

---

勇者，請幫香香阿福判斷出它可以生產出的最好練度吧 !!!  

## 輸入說明
多筆測資( $a_i$ )，以EOF結尾  
每筆測資有兩個字串 $r$ 及 $k$  
其分別代表機器判斷的資料及程度  
* 每條生產線初始練度均為 $0$
* 生產線從第一條算起
* 若機器過熱 $(E)$ ，當條生產線練度則算到過熱前，且程度 $(k_i)$ 必為 $0$
* 若機器總練度為負，當條生產線報廢不算

## 輸出說明
輸出兩行  
第一行輸出最好練度，第二行則為第幾條生產線  
若沒有生產線符合則輸出 "Chop off!!" (不含引號) 

## 輸入限制
* $a_i \leq 10^3$
* $len(r)=len(k)$
* $0 \le k_i \le 9$

## 子任務
| Subtask | Score | Contraints 
|-|-|-
| 1 | 30 | 單筆測資 $i=1$
| 2 | 10 | 所有生產線練度均 $\geq 0$
| 3 | 60 | 題目說明，無特別條件

## 範例輸入 1
```
BBAA
5277
```

## 範例輸出 1
```
7
1
```

## 範例輸入 2

```
AABB
5277
ABCDE
12340
```

## 範例輸出 2
```
Chop off!!
```

## 範例說明
範例一中執行序為 $(BBAA,5277)=0-5-2+7+7=7$  
因為只有一條生產線，因此最佳生產線為它  

範例二中第一條生產線執行序為 $(AABB,5277)=0+5+2-7-7=-7$ 此條生產線報廢  
第二條生產線執行序為 $(ABCDE,12340)=0+1-2\times3\div4=-\frac{3}{4}$ 此條生產線也報廢  
因此此筆測資沒有一條符合因此輸出 "Chop off!!"