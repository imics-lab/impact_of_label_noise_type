#Author: Gentry Atkinson
#Organization: Texas University
#Data: 19 December, 2021
#Avoiding divide by zeros errors with the greatest of ease

cnn_cm_dic = {
    'SS1 Clean':
    [[829, 182],
     [121, 868]],

     'SS1 NCAR5':
     [[848, 152],
      [296, 704]],

    'SS1 NCAR10':
    [[764, 234],
     [329, 673]],

    'SS1 NAR5':
    [[680, 235],
    [194 ,891]],

    'SS1 NAR10':
    [[518, 276],
     [229, 977]],

    'SS1 NNAR5':
    [[658, 253],
     [148, 941]],

    'SS1 NNAR10':
    [[607, 204],
     [236, 953]],

    'SS2 Clean':
    [[965, 209,   6,   0,   0],
     [190, 788, 191,   5,   5],
     [  7, 206, 706, 245,  27],
     [  1,  13, 262, 620, 360],
     [  3,   6,  43, 208, 934]],

    'SS2 NCAR5':
    [[898, 242,  20,  10,  26],
    [198, 749, 192,  26,  16],
    [ 15, 198, 665, 267,  33],
    [ 14,  21, 231, 692, 293],
    [ 17,  18,  49, 266, 844]],

    'SS2 NCAR10':
    [[805, 249,  35,  43,  70],
     [172, 681, 244,  57,  39],
     [ 30, 169, 613, 330,  61],
     [ 21,  38, 203, 590, 357],
     [ 24,  32,  60, 251, 826]],

    'SS2 NAR5':
    [[1018,  157,    3,    0,    2],
     [ 271,  703,  259,  165,   93],
     [   7,  152,  742,  267,   23],
     [   0,    6,  183,  507,  248],
     [   3,   9,   36,  247,  899]],

     'SS2 NAR10':
     [[1095,   77,    8,    0,    0],
      [ 410,  542,  316,  367, 151],
      [  23 , 143,  761,  254,   10],
      [   1,    2,  119,  383,  144],
      [   5 ,   4,   28 , 251 , 906]],

    'SS2 NNAR5':
    [[1030,  140 ,   7 ,   0  ,  3],
     [ 289,  656 , 272  ,182 ,  80],
     [  14 , 157,  742 , 259  , 19],
     [   3  , 10 , 190  ,548,  205],
     [   3 ,   7 ,  36,  247 , 901]],

    'SS2 NNAR10':
    [[1048,  129,    3,    0,    0],
     [ 370,  553,  373 , 360 , 123],
     [  48 ,  90  ,748 , 293 ,  12],
     [   2 ,   2 ,  91,  457,  104],
     [   5,    5,   30 , 359,  795]],

    'BS1 Clean':
    [[7007, 3692],
    [4018, 2526]],

    'BS1 NCAR5':
    [[6510, 4019],
     [4019, 2695]],

    'BS1 NCAR10':
    [[6536, 3709],
    [4212, 2786]],

    'BS1 NAR5':
    [[5260, 4511],
     [3748, 3724]],

    'BS1 NAR10':
    [[4518, 4381],
     [3909, 4435]],

    'BS1 NNAR5':
    [[5945, 3891],
     [4155, 3252]],

    'BS1 NNAR10':
    [[4913, 4061],
    [4362, 3907]],

    BS2 Clean
    [[ 30 637]
     [ 25 780]]

    BS2 NCAR5
    [[147 516]
     [154 655]]

    BS2 NCAR10
    [[ 93 599]
     [100 680]]

    BS2 NAR5
    [[101 639]
     [ 56 676]]

    BS2 NAR10
    [[126 693]
     [ 80 573]]

    BS2 NNAR5
    [[ 12 729]
     [ 12 719]]

    BS2 NNAR10
    [[132 683]
     [105 552]]

    HAR1 Clean
    [[ 69   3   0   7  65  29]
    [  0 116  55   0   0   2]
    [  1   0 141  28   1   0]
    [ 21   2  32 120  10   1]
    [  5   0   0   8 139  46]
    [  1   0   2   5   8 174]]

    HAR1 NCAR5
    [[ 66   4   6   6  66  23]
     [  0  73  96   3   3   0]
     [  2   1 127  25   6   5]
     [ 21   1  23 114  25   6]
     [  7   1   4   7 138  41]
     [  1   0   7   3  12 168]]

    HAR1 NAR5
    [[ 88   3   0   6  46  30]
    [  0  59  31  75   0   8]
    [ 14   0 144  26  39  13]
    [ 26   1  16 134   8   1]
    [ 23   0   0   8  78  24]
    [  2   0   1   5   5 177]]

    HAR1 NAR10
    [[127   4   0   6  10  26]
     [  0  45 127   0   0   1]
     [ 65   0 145  26  21  24]
     [ 40   3  27 114   0   2]
     [ 56   0   0   5  14  13]
     [ 13   0   2   5   3 167]]

    HAR1 NNAR5
    [[ 80   3   0   4  62  24]
     [  0  48 124   0   0   1]
     [ 14   0 144  24  32  12]
     [ 45   2  25 106   4   4]
     [ 28   0   0   0  99  16]
     [  7   0   4   3   3 173]]

    HAR1 NNAR10
    [[118   3   0   6  14  32]
     [  0  96  77   0   0   0]
     [ 36   0 145  23  34  43]
     [ 47   2  27 105   2   3]
     [ 35   0   0   5  29  19]
     [  8   0   4   4   2 172]]

    HAR2 Clean
    [[425  16  51   1   3   0]
    [ 89 334  26   2  20   0]
    [  2  36 372   5   5   0]
    [  1   1   0 336 147   6]
    [  0   0   0  77 455   0]
    [  0   0   0   4   0 533]]

    HAR2 NCAR5
    [[403  38  25   8  16   5]
     [105 315  20  10  19   4]
     [ 80  42 276   4  16   4]
     [ 13   9   5 300 159   3]
     [ 12   7   3  41 462   6]
     [  4   4   2  16   9 502]]

    HAR2 NCAR10
    [[351  59  32   8  28  13]
     [ 66 338  20  13  29  18]
     [ 49  59 275  12  27  11]
     [ 14   5   6 274 163  23]
     [ 13   8   3  69 416  14]
     [ 11   5   8  11  12 484]]

    HAR2 NAR5
    [[451  15  23   5   2   0]
     [ 70 369  17   8   7   0]
     [ 20  26 365  11   0 154]
     [  0   1   0 371 115   4]
     [  0   0   0  69 463   0]
     [  0   0  12   2   0 367]]

    HAR2 NAR10
    [[464  11  19   0   2   0]
     [107 343  11   0  10   0]
     [ 47  43 569   5   4  55]
     [  2   2   0 309 176   2]
     [  0   1   0  52 479   0]
     [  0   0 182   9   0  43]]

    HAR2 NNAR5
    [[444  16  35   1   0   0]
     [106 323  33   1   8   0]
     [  5  28 407   2   0 126]
     [  0   3   1 326 159   2]
     [  1   0   0  53 478   0]
     [  0   0  36   3   0 350]]

    HAR2 NNAR10
    [[450  15  26   2   3   0]
     [113 282  15   7  54   0]
     [ 38  76 368  20   0 213]
     [  2   1   0 359 127   2]
     [  0   0   0  60 472   0]
     [  0   0  47  18   0 177]]
}
##### LSTM
SS1 Clean
[[645 366]
 [120 869]]

SS1 NCAR5
[[619 381]
 [181 819]]

SS1 NCAR10
[[574 424]
 [209 793]]

SS1 NAR5
[[526 389]
 [137 948]]

SS1 NAR10
[[506 288]
 [294 912]]

SS1 NNAR5
[[607 304]
 [162 927]]

SS1 NNAR10
[[506 305]
 [213 976]]

SS2 Clean
[[994 180   5   0   1]
 [228 730 208  11   2]
 [  5 181 594 352  59]
 [  0  11 193 666 386]
 [  4   9  41 266 874]]

 SS2 NCAR5
 [[841 291  29  12  23]
  [147 675 309  26  24]
  [ 10 149 622 302  95]
  [  9  26 204 611 401]
  [ 10  21  48 261 854]]

SS2 NACAR10
[[728 339  40  35  60]
 [118 678 302  53  42]
 [ 24 128 615 292 144]
 [ 17  39 168 492 493]
 [ 27  31  65 173 897]]

SS2 NAR5
[[809 347  22   0   2]
 [151 599 421 182 138]
 [  1  70 612 392 116]
 [  0   4 109 433 398]
 [  3   4  29 200 958]]

SS2 NAR10
[[1089   72   19    0    0]
 [ 553  240  459  318  216]
 [  44   43  663  347   94]
 [   2    1   91  300  255]
 [   4    1   39  256  894]]

SS2 NNAR5
[[903 260  15   1   1]
 [193 603 404 195  84]
 [  7  80 673 379  52]
 [  0   6 142 551 257]
 [  4   4  39 329 818]]

SS2 NNAR10
[[1043  123   12    0    2]
 [ 460  394  413  271  241]
 [  38   91  669  298   95]
 [   2    1   95  295  263]
 [   4    4   36  179  971]]

BS1 Clean
[[6048 4651]
 [3361 3183]]

BS1 NCAR5
[[6580 3949]
 [3984 2730]]

BS1 NCAR10
[[5783 4462]
 [3709 3289]]

BS1 NAR5
[[5203 4568]
 [3690 3782]]

BS1 NAR10
[[4453 4446]
 [3967 4377]]

BS1 NNAR5
[[5251 4585]
 [3765 3642]]

BS1 NNAR10
[[4404 4570]
 [3758 4511]]

BS2 Clean
[[138 529]
 [149 656]]

BS2 NCAR5
[[ 13 650]
 [  9 800]]

BS2 NCAR10
[[189 503]
 [214 566]]

BS2 NAR5
[[156 584]
 [140 592]]

BS2 NAR10
[[158 661]
 [126 527]]

BS2 NNAR5
[[144 597]
 [164 567]]

BS2 NNAR10
[[216 599]
 [150 507]]

HARR1 Clean
[[ 72   3   1   6  52  39]
 [  0  71 102   0   0   0]
 [  0   1 142  27   1   0]
 [ 29   2  32 104  18   1]
 [  9   0   0   4 136  49]
 [  0   1   6   3   5 175]]

HAR1 NCAR5
[[ 69   5   6   6  56  29]
 [  0 105  66   2   1   1]
 [  1   1 115  39   4   6]
 [ 21   3  20 121  21   4]
 [ 10   2   3  12 128  43]
 [  0   0   5   2  14 170]]

HAR1 NCAR10
[[ 67   6   2  12  60  36]
 [  1  95  63   4   6   3]
 [  2   2 117  40   9   3]
 [ 20   6  22 109  12   8]
 [ 11   4   5   9 120  41]
 [  0   3   6   8  17 162]]

HAR1 NAR5
[[ 89   3   0  11  37  33]
 [  0 123  50   0   0   0]
 [ 12   0 144  27  36  17]
 [ 22   1  31 118  13   1]
 [  4   1   0   4  91  33]
 [  4   0   4   1   3 178]]

HAR1 NAR10
[[123   3   0  10   6  31]
 [  0 122  51   0   0   0]
 [ 62   0 146  25  17  31]
 [ 44   2  31 108   0   1]
 [ 47   1   0   3  18  19]
 [ 14   1   5   5   0 165]]

HAR1 NNAR5
[[ 66   4   0   9  51  43]
 [  0  65 108   0   0   0]
 [  3   0 145  28  22  28]
 [ 16   3  38 119   8   2]
 [  7   0   2  10  90  34]
 [  1   0   9   3   6 171]]

HAR1 NNAR10
[[123   3   0   9   3  35]
 [  0 113  60   0   0   0]
 [ 61   0 141  38   6  35]
 [ 41   3  27 112   0   3]
 [ 62   0   0   2   7  17]
 [  9   0   5   3   0 173]]

HAR2 Clean
[[444  23  29   0   0   0]
 [ 90 364  17   0   0   0]
 [ 25  25 370   0   0   0]
 [  0   0   0 350 141   0]
 [  0   0   0  55 477   0]
 [  0   0   0  51   1 485]]

HAR2 NCAR5
[[336  87  53   5   7   7]
 [ 46 375  34   6   5   7]
 [ 10  38 355   3  11   5]
 [  8  10   6 257 163  45]
 [ 11   6   6  41 461   6]
 [  2   4   4   6   9 512]]

HAR2 NCAR10
[[315  79  56   6  20  15]
 [ 62 359  30   7  11  15]
 [ 18  48 332   6  14  15]
 [  8   9   9 202 129 128]
 [  9  10   5  62 420  17]
 [  8   4  13   9  11 486]]

HAR2 NAR5
[[395  50  49   0   2   0]
 [107 343  21   0   0   0]
 [ 31  27 362  27   0 129]
 [  0   0   0 352 138   1]
 [  0   0   0  83 449   0]
 [  0   0   0  69   0 312]]

HAR2 NAR10
[[404  57  32   0   3   0]
 [ 97 352  19   1   2   0]
 [ 26  34 611  47   0   5]
 [  0   1   0 355 135   0]
 [  1   0   0  59 472   0]
 [  0   0 187  42   0   5]]

HAR2 NNAR5
[[392  69  35   0   0   0]
 [ 74 373  21   1   2   0]
 [ 26  28 366  36   2 110]
 [  0   0   0 356 135   0]
 [  0   0   0  85 447   0]
 [  0   0   0 103   0 286]]

HAR2 NNAR10
[[394  55  47   0   0   0]
 [ 71 367  31   1   1   0]
 [ 15  16 497   9   1 177]
 [  0   0   0 332 158   1]
 [  0   0   0  34 497   1]
 [  0   0  95   6   0 141]]

##### SVM
SS1 Clean
[[976  35]
 [ 53 936]]

SS1 NCAR5
[[932  68]
 [101 899]]

SS1 NCAR10
[[884 114]
 [160 842]]

SS1 NAR5
[[877  38]
 [142 943]]

SS1 NAR10
[[756  38]
 [247 959]]

SS1 NNAR5
[[879  32]
 [101 988]]

SS1 NNAR10
[[ 783   28]
 [ 176 1013]]

SS2 Clean
[[1138   42    0    0    0]
 [  68 1034   77    0    0]
 [   3  145  799  229   15]
 [   0   23  234  593  406]
 [   6   17   71  278  822]]

SS2 NCAR5
[[1088   65   13    9   21]
 [  73  995   87   11   15]
 [  14  152  767  216   29]
 [  10   42  228  575  396]
 [  18   30   74  276  796]]

SS2 NCAR10
[[1023   74   24   41   40]
 [  84  953   99   31   26]
 [  35  165  744  213   46]
 [  27   48  221  528  385]
 [  34   36  100  271  752]]

SS2 NAR5
[[1156   24    0    0    0]
 [ 111  967  162  143  108]
 [   4  129  814  229   15]
 [   0   16  180  450  298]
 [   7   15   72  278  822]]

SS2 NAR10
[[1180    0    0    0    0]
 [ 604  432  270  282  198]
 [  36   74  837  229   15]
 [   4    5  121  311  208]
 [  17    3   74  278  822]]

SS2 NNAR5
[[1156   24    0    0    0]
 [ 109  937  207  128   98]
 [   4  119  824  229   15]
 [   0   13  170  465  308]
 [   7   13   74  278  822]]

SS2 NNAR10
[[1168   12    0    0    0]
 [ 198  838  304  236  203]
 [  18   91  838  229   15]
 [   0    4   92  357  203]
 [   9   11   74  278  822]]

BS1 Clean
[[5666 5033]
 [2946 3598]]

BS1 NCAR5
[[5705 4824]
 [3298 3416]]

BS1 NCAR10
[[5813 4432]
 [3670 3328]]

BS1 NAR5
[[4397 5374]
 [2512 4960]]

BS1 NAR10
[[3633 5266]
 [2152 6192]]

BS1 NNAR5
[[4500 5336]
 [2501 4906]]

BS1 NNAR10
[[3695 5279]
 [2231 6038]]

BS2 Clean
[[  0 667]
 [  0 805]]

BS2 NCAR5
[[  0 663]
 [  0 809]]

BS2 NCAR10
[[  0 692]
 [  0 780]]

BS2 NAR5
[[  0 740]
 [  0 732]]

BS2 NAR10
[[  0 819]
 [  0 653]]

BS2 NNAR5
[[  0 741]
 [  0 731]]

BS2 NNAR10
[[  0 815]
 [  0 657]]

HAR1 Clean
[[144   0   0   0  18  11]
 [  0 173   0   0   0   0]
 [  0   0 138  30   3   0]
 [  0   0  13 172   1   0]
 [ 33   0   0   0  87  78]
 [ 24   5   0   0   2 159]]

HAR1 NCAR5
[[136   2   6   0  15  12]
 [  0 169   2   1   2   1]
 [  4   1 125  29   3   4]
 [  5   0  15 166   2   2]
 [ 35   1   3   5  77  77]
 [ 13   5   1   0   4 168]]

HAR1 NCAR10
[[136   3   1   6  21  16]
 [  2 157   2   3   5   3]
 [  1   3 136  24   3   6]
 [  3   4  18 148   1   3]
 [ 30   5   2   4 100  49]
 [ 20   6   4   5   4 157]]

HAR1 NAR5
[[158   0   0   0   4  11]
 [  0 173   0   0   0   0]
 [ 34   0 138  31   5  28]
 [  0   0  13 172   1   0]
 [ 62   0   0   0  14  57]
 [ 14   5   0   0   0 171]]

HAR1 NAR10
[[161   0   0   0   0  12]
 [  0 173   0   0   0   0]
 [ 72   0 138  31   0  40]
 [  0   0  13 172   0   1]
 [ 61   0   0   0   0  27]
 [ 12   5   0   0   0 173]]

HAR1 NNAR5
[[155   0   0   0   4  14]
 [  0 173   0   0   0   0]
 [ 31   0 138  30   6  21]
 [  0   0  13 172   1   0]
 [ 67   0   0   0  18  58]
 [ 10   5   0   0   0 175]]

HAR1 NNAR10
[[160   0   0   0   0  13]
 [  0 173   0   0   0   0]
 [ 76   0 138  31   0  36]
 [  0   0  13 172   0   1]
 [ 54   0   0   0   0  34]
 [ 13   5   0   0   0 172]]

HAR2 Clean
[[461   6  11   5  10   2]
 [ 90 349  16   2  10   6]
 [203  27 173   0  17   2]
 [  9  10   3 120 295  52]
 [ 14   3   3  72 421  18]
 [  7   2   1 137 137 253]]

HAR2 NCAR5
[[464   6   8   5  10   2]
 [ 89 351  15   2  10   6]
 [203  27 173   0  17   2]
 [  9  10   3 113 305  49]
 [ 14   3   3  70 425  16]
 [  7   2   1 133 147 247]]

HAR2 NCAR10
[[444   7   6   6  22   6]
 [ 96 350  10   5  19   4]
 [243  33 123  13  18   3]
 [ 17   8   1 128 284  47]
 [ 16   7   1  84 398  17]
 [ 22   2   2 134 127 244]]

HAR2 NAR5
[[477   3  16   0   0   0]
 [ 89 339  43   0   0   0]
 [206  21 194  44  39  72]
 [  0   1   0 127 313  50]
 [  0   0   0  74 450   8]
 [  0   0   0  97 107 177]]

HAR2 NAR10
[[468   3  25   0   0   0]
 [ 93 330  48   0   0   0]
 [204  16 336  81  86   0]
 [  0   1  48 127 315   0]
 [  0   0   3  74 455   0]
 [  0   0  96  64  74   0]]

HAR2 NNAR5
[[478   3  15   0   0   0]
 [ 91 342  38   0   0   0]
 [213  21 186  41  38  69]
 [  0   1   0 127 313  50]
 [  0   0   0  74 451   7]
 [  0   0   1 103 109 176]]

HAR2 NNAR10
[[475   3  18   0   0   0]
 [ 93 332  46   0   0   0]
 [210  19 325  89  72   0]
 [  0   1  48 127 315   0]
 [  0   0   3  73 456   0]
 [  0   0  99  58  85   0]]

##### NB
SS1 Clean
[[946  65]
 [ 39 950]]

SS1 NCAR5
[[915  85]
 [ 95 905]]

SS1 NCAR10
[[875 123]
 [156 846]]

SS1 NAR5
[[851  64]
 [127 958]]

SS1 NAR10
[[729  65]
 [229 977]]

SS1 NNAR5
[[875  36]
 [ 98 991]]

SS1 NNAR10
[[ 775   36]
 [ 165 1024]]

SS2 clean
[[1110   70    0    0    0]
 [  46  966  165    1    1]
 [   0  129  631  429    2]
 [   0   24  185 1041    6]
 [   6   15   54 1107   12]]

SS2 NCAR5
[[1106   40   34   16    0]
 [  92  747  332    7    3]
 [  14   84 1047   31    2]
 [  10   33  853  346    9]
 [  20   17  471  668   18]]

SS2 NCAR10
[[1039   52   25   83    3]
 [ 119  825  185   63    1]
 [  35  144  596  425    3]
 [  28   49  177  948    7]
 [  37   34   79 1028   15]]

SS2 NAR5
[[1141   39    0    0    0]
 [  69  946  213  261    2]
 [   2  121  636  429    3]
 [   0   17  141  781    5]
 [   8   13   54 1107   12]]

SS2 NAR10
[[1145   35    0    0    0]
 [  75  938  266  501    6]
 [   3  120  636  429    3]
 [   0   13   94  541    1]
 [   8   14   54 1107   11]]

SS2 NNAR5
[[1151   29    0    0    0]
 [  88  922  228  239    2]
 [   3  117  639  429    3]
 [   0   16  132  803    5]
 [   8   12   55 1107   12]]

SS2 NNAR10
[[1157   23    0    0    0]
 [ 124  888  295  466    6]
 [   4  114  641  429    3]
 [   0    5   72  576    3]
 [   9   11   55 1107   12]]

BS1 Clean
[[1047 9652]
 [ 474 6070]]

BS1 NCAR5
[[1017 9512]
 [ 504 6210]]

BS1 NCAR5
[[1163 9366]
 [ 636 6078]]

BS1 NCAR10
[[1118 9127]
 [ 658 6340]]

BS1 NAR5
[[1065 8706]
 [ 689 6783]]

BS1 NAR10
[[ 745 8154]
 [ 502 7842]]

BS1 NNAR5
[[ 899 8937]
 [ 512 6895]]

BS1 NNAR10
[[ 911 8063]
 [ 734 7535]]

BS2 Clean
[[ 23 644]
 [  2 803]]

BS2 NCAR5
[[ 21 642]
 [  4 805]]

BS2 NCAR10
[[ 19 673]
 [  5 775]]

BS2 NAR5
[[ 23 717]
 [  2 730]]

BS2 NAR10
[[ 23 796]
 [  2 651]]

BS2 NNAR5
[[ 24 717]
 [  1 730]]

BS2 NNAR10
[[ 23 792]
 [  2 655]]

HAR1 Clean
[[141   0   0   0  14  18]
 [  0  58   0   0   3 112]
 [  1   0 152  14   4   0]
 [  3   0 110  66   2   5]
 [ 43   0   0   0 115  40]
 [  3   0   0   0   8 179]]

HAR1 NCAR5
[[134   2   6   0  18  11]
 [  1 162   3   0   8   1]
 [  3   1 148   7   2   5]
 [  2   0 151  29   6   2]
 [ 49   1   7   3 127  11]
 [  7   0   1   0  14 169]]

HAR1 NCAR10
[[137   3   2   5  20  16]
 [  4 149   0   5   9   5]
 [  1   2  88  73   4   5]
 [  2   4  21 144   2   4]
 [ 47   5   2   7 101  28]
 [ 18   3   3   6  14 152]]

HAR1 NAR5
[[148   0   0   0   9  16]
 [  0  58   0   0   3 112]
 [ 35   0 152  14  24  11]
 [ 10   0 110  65   0   1]
 [ 48   0   0   0  56  29]
 [  6   0   0   0  10 174]]

HAR1 NAR10
[[151   0   0   0   6  16]
 [  4  58   0   0   0 111]
 [ 41   0 152  14  51  23]
 [ 10   0 110  65   0   1]
 [ 21   0   0   0  56  11]
 [ 14   0   0   0   1 175]]

HAR1 NNAR5
[[140   0   0   0  16  17]
 [  2  58   0   0   0 113]
 [ 17   0 152  14  29  14]
 [  9   0 110  66   0   1]
 [ 17   0   0   0 106  20]
 [ 13   0   0   0   1 176]]

HAR1 NNAR10
[[144   0   0   0  13  16]
 [  4  58   0   0   0 111]
 [ 27   0 152  14  62  26]
 [ 10   0 110  65   0   1]
 [ 16   0   0   0  57  15]
 [ 14   0   0   0   1 175]]

HAR2 Clean
[[485   1  10   0   0   0]
 [ 92 372   7   0   0   0]
 [ 97  15 308   0   0   0]
 [  0   1   0  88 388  14]
 [  0   0   0  56 455  21]
 [  1   1   0 198 178 159]]

HAR2 NCAR5
[[467   4   7   6   9   2]
 [108 338   9   5   8   5]
 [132   7 264   2  15   2]
 [ 10   7   4 114 305  49]
 [ 12   4   4  90 414   7]
 [  6   1   3 180 119 228]]

HAR2 NCAR10
[[436   7  14   1  26   7]
 [129 314  13   0  23   5]
 [121  12 266   2  28   4]
 [ 12   5   8  23 390  47]
 [ 13   7   4  11 478  10]
 [ 17   3   6  36 233 236]]

HAR2 NAR5
[[489   1   6   0   0   0]
 [ 94 369   8   0   0   0]
 [162  39 221  58  55  41]
 [  0   0   2  91 388  10]
 [  0   0   2  57 456  17]
 [  0   0   1 150 123 107]]

HAR2 NAR10
[[490   1   5   0   0   0]
 [ 94 371   6   0   0   0]
 [182  56 183 125  99  78]
 [  0   0   1  91 388  11]
 [  0   0   2  57 457  16]
 [  0   0   2  93  79  60]]

HAR2 NNAR5
[[489   1   6   0   0   0]
 [ 94 369   8   0   0   0]
 [166  44 211  61  45  41]
 [  0   0   1  91 388  11]
 [  0   0   2  57 455  18]
 [  0   0   2 148 133 106]]

HAR2 NNAR10
[[490   1   5   0   0   0]
 [ 94 373   4   0   0   0]
 [186  59 178  74  94 124]
 [  0   0   6  59 389  37]
 [  0   0  11  55 460   6]
 [  0   0   1  69  85  87]]

##### RF
SS1 clean
[[978  33]
 [ 62 927]]

SS1 NCAR5
[[926  74]
 [110 890]]

SS1 NCAR10
[[878 120]
 [173 829]]

SS1 NAR5
[[873  42]
 [145 940]]

SS1 NAR10
[[731  63]
 [245 961]]

SS1 NNAR5
[[881  30]
 [108 981]]

SS1 NNAR10
[[ 759   52]
 [ 177 1012]]

SS2 clean
[[1130   50    0    0    0]
 [  84 1015   75    4    1]
 [   2  147  883  155    4]
 [   0   14  249  777  216]
 [   4   11   28  298  853]]

SS2 NCAR5
[[1086   66   13   15   16]
 [  87  989   80   11   14]
 [  16  172  819  157   14]
 [   9   40  243  730  229]
 [  16   27   40  291  820]]

SS2 NCAR10
[[1022   68   34   42   36]
 [ 102  950   86   37   18]
 [  33  173  785  180   32]
 [  30   38  258  650  233]
 [  35   42   59  261  796]]

SS2 NAR5
[[1143   36    0    0    1]
 [ 244  842  155  188   62]
 [  20  116  899  152    4]
 [   6   11  186  577  164]
 [   7    8   39  261  879]]

SS2 NAR10
[[1175    5    0    0    0]
 [ 667  424  215  391   89]
 [  83   55  895  154    4]
 [   5    4  134  396  110]
 [   6   12   38  287  851]]

SS2 NNAR5
[[1158   21    0    0    1]
 [ 202  874  178  165   60]
 [  36  100  896  155    4]
 [   3    7  164  630  152]
 [   5    9   33  281  866]]

SS2 NNAR10
[[1174    6    0    0    0]
 [ 541  562  236  333  107]
 [  95   46  878  165    7]
 [   4    1  110  433  108]
 [  12    3   31  296  852]]

BS1 clean
[[8582 2117]
 [3733 2811]]

BS1 NCAR5
[[8336 2193]
 [4048 2666]]

BS1 NCAR10
[[8230 2015]
 [4521 2477]]

BS1 NAR5
[[7170 2601]
 [4072 3400]]

BS1 NAR10
[[5898 3001]
 [4006 4338]]

BS1 NNAR5
[[7414 2422]
 [4043 3364]]

BS1 NNAR10
[[6178 2796]
 [4019 4250]]

BS2 Clean
[[238 429]
 [377 428]]

BS2 NCAR5
[[228 435]
 [402 407]]

BS2 NCAR10
[[242 450]
 [376 404]]

BS2 NAR5
[[262 478]
 [355 377]]

BS2 NAR10
[[360 459]
 [350 303]]

BS2 NNAR5
[[267 474]
 [360 371]]

BS2 NNAR10
[[339 476]
 [344 313]]

HAR1 clean
[[124   3   0   0  23  23]
 [  1  28   0   0   0 144]
 [  1   0 138  31   0   1]
 [  0   0  44 142   0   0]
 [ 24   0   0   0 138  36]
 [  1   3   0   0   1 185]]

HAR1 NCAR5
[[114   3   3   3  29  19]
 [ 18 126   2   1   2  26]
 [  5   1 130  23   1   6]
 [  3   0  21 161   2   3]
 [ 27   0   4   5 138  24]
 [  7   1   1   1   8 173]]

HAR1 NCAR10
[[122   8   2   5  22  24]
 [  7 134   1   5   5  20]
 [  2   2 126  33   3   7]
 [  1   3  30 134   2   7]
 [ 30   4   3   3 122  28]
 [  8   7   2   7   5 167]]

HAR1 NAR5
[[135   3   0   0  11  24]
 [  0  24   0   0   0 149]
 [ 21   0 147  21  33  14]
 [  0   0  32 154   0   0]
 [ 42   1   0   0  62  28]
 [  5   1   0   0   1 183]]

HAR1 NAR10
[[153   4   0   0   2  14]
 [  0 172   0   0   0   1]
 [ 90   0 148  20   7  16]
 [  0   0  23 163   0   0]
 [ 70   0   0   0   9   9]
 [  7   2   0   0   0 181]]

HAR1 NNAR5
[[139   4   0   0   6  24]
 [  0 151   0   0   0  22]
 [ 28   0 139  29  10  20]
 [  0   0  23 163   0   0]
 [ 95   0   0   0  32  16]
 [  4   2   0   0   1 183]]

HAR1 NNAR10
[[143   2   0   0   6  22]
 [  0  14   0   0   0 159]
 [ 72   2 134  34  17  22]
 [  0   0  31 155   0   0]
 [ 53   0   0   0  17  18]
 [  9   3   0   0   0 178]]

 HAR2 clean
 [[487   5   4   0   0   0]
  [ 66 366  39   0   0   0]
  [ 55  23 342   0   0   0]
  [  0   0   0 239 187  65]
  [  0   0   0 165 321  46]
  [  0   0   1 128  75 333]]

HAR2 NCAR5
[[454   8  16  10   5   2]
 [ 78 336  41   8   4   6]
 [ 57  29 317   5  10   4]
 [  7   6   9 251 162  54]
 [ 12   6   5 145 331  32]
 [  5   4   4 137  88 299]]

HAR2 NCAR10
[[432   6  19  10  12  12]
 [ 85 325  46   9  13   6]
 [ 64  35 299  19  12   4]
 [ 13   4   8 214 181  65]
 [ 12   9   5 117 323  57]
 [ 14   2  10 120  77 308]]

HAR2 NAR5
[[487   3   6   0   0   0]
 [ 71 370  30   0   0   0]
 [ 57  31 341  49  22  76]
 [  0   1  11 230 199  50]
 [  0   0   3 155 349  25]
 [  0   0  27  90  71 193]]

HAR2 NAR10
[[481   4  11   0   0   0]
 [ 67 379  25   0   0   0]
 [ 52  26 443  84  46  72]
 [  0   0  37 233 199  22]
 [  0   0  30 162 331   9]
 [  0   0  94  55  44  41]]

HAR2 NNAR5
[[480   6  10   0   0   0]
 [ 68 358  45   0   0   0]
 [ 50  27 364  38  26  63]
 [  0   0   9 245 173  64]
 [  0   0   2 169 334  27]
 [  0   0  44 104  67 174]]

HAR2 NNAR10
[[485   5   6   0   0   0]
 [ 76 364  31   0   0   0]
 [ 63  29 449  78  45  51]
 [  0   0  31 268 161  31]
 [  0   0  21 170 331  10]
 [  1   0  92  55  45  49]]

##### Transformer
SS1 Clean
[[979  48]
[147 826]]

SS1 NCAR5
[[843 188]
 [131 838]]

SS1 NAR5
[[812 105]
 [221 862]]

SS1 NAR10
[[770  64]
 [348 818]]

SS1 NNAR5
[[903  70]
 [138 889]]

SS1 NNAR10
[[899  58]
 [145 898]]

SS2 Clean
[[1127   60    0    0    0]
 [ 170  891  101    3    0]
 [   2  204  842  168    3]
 [   2   28  338  608  209]
 [  14    6   74  299  851]]

SS2 NCAR5
[[1079   61    9    8   23]
 [ 188  836  116   12   26]
 [  23  249  696  207   46]
 [  28   55  265  426  416]
 [  29   32   77  163  930]]

SS2 NCAR10
[[905 188  26  19  42]
 [149 773 180  25  38]
 [ 33 209 708 230  63]
 [ 37  53 264 437 378]
 [ 37  42  90 211 863]]

SS2 NAR5
[[946 240   0   1   0]
 [ 70 971 144  57 216]
 [  0 191 791 232   5]
 [  0  35 260 650 240]
 [  8   6  52 223 662]]

SS2 NAR10
[[1088   98    1    0    0]
 [ 215  902   73  129  448]
 [  14  314  558  329    4]
 [   5   32  170  704  274]
 [   7    8   19  153  455]]

SS2 NNAR5
[[1092   99    0    0    0]
 [ 134  955   81    4    0]
 [   1  271  642  345   13]
 [   2   42  177  710  470]
 [   6    7   18  141  790]]

SS2 NNAR10
[[1180   14    0    0    0]
 [ 289  849   37    4    0]
 [   5  375  483  432    4]
 [   5   52  145 1018  348]
 [   4    4    3  124  625]]

BS1 Clean
[[10456     0]
 [ 6544     0]]

BS1 NCAR5
[[10312     0]
 [ 6688     0]]

BS1 NCAR10
[[10012     0]
 [ 6988     0]]

BS1 NAR5
[[9579    0]
 [7421    0]]

BS1 NAR10
[[8665    0]
 [8335    0]]

BS1 NNAR5
[[10456     0]
 [ 6544     0]]

BS1 NNAR10
[[10456     0]
 [ 6544     0]]

BS2 Clean
[[304   0]
 [396   0]]

BS2 NCAR5
[[145  14]
 [  6  35]]

BS2 NCAR10
[[307   0]
 [393   0]]

BS2 NAR5
[[344   0]
 [356   0]]

BS2 NAR10
[[377   0]
 [323   0]]

BS2 NNAR5
[[319   0]
 [381   0]]

BS2 NNAR10
[[371   0]
 [329   0]]

HAR1 Clean
[[ 83   0   0   0  85   5]
 [  4 169   0   0   0   0]
 [  0   0 141  39   0   0]
 [  0   0 105  65  16   0]
 [ 11   0   0   0 185   2]
 [  7  10   0   0   9 164]]

HAR1 NCAR5
[[107   1   1   0  57   3]
 [ 12 146   2   2  13   1]
 [  8   2  78  89   7   1]
 [ 38   1  37 104   6   2]
 [ 48   0   0   0 143   1]
 [ 20   9   5   4  37 115]]

HAR1 NCAR10
[[ 78   4  14   5  70   9]
 [  7 148   7   2   4   8]
 [  1   4  91  55   6   8]
 [  0   3 125  34   8  12]
 [ 24   5   5   0 163   7]
 [  4  14   8   4  11 152]]

HAR1 NAR5
[[ 91   0   0   0  82   0]
 [  4 167   0   0   0   2]
 [ 12   0 115  62  55   0]
 [ 25   0 107  53   0   1]
 [ 17   0   0   0 117   0]
 [ 10   5   2   0   7 166]]

HAR1 NAR10
[[154   0   0   0  19   0]
 [  5 166   0   0   0   2]
 [ 69   0  86  94  33   0]
 [ 25   1  65  83   0  12]
 [ 67   0   0   0  29   0]
 [ 10   6   0   0   3 171]]

HAR1 NNAR5
[[111   0   0   0  62   0]
 [  0 163   0   0   5   5]
 [ 14   1 147  29  41   3]
 [  0   0  94  64   0  28]
 [ 33   0   0   0 105   5]
 [  5   3   0   0   1 181]]

HAR1 NNAR10
[[173   0   0   0   0   0]
 [  4 167   0   0   0   2]
 [127   0  87  76   0   0]
 [ 25   0 120  28  13   0]
 [ 88   0   0   0   0   0]
 [  2   6   2   1   0 179]]

HAR2 Clean
[[267  84  85  60   0   0]
 [  4 314  96   0  27   0]
 [ 41 163 153  15  31   0]
 [ 14  25   9 348  90   5]
 [  0  59  20   0 453   0]
 [  0   0   0   0   0 537]]

HAR2 NCAR5
[[308 158   6  18   5   3]
 [  7 347   4   3  79   7]
 [ 54 271  45   6  23   4]
 [ 29  15  12 326  93  23]
 [  4  10  22  20 466   5]
 [  2   4   0   5   2 514]]

HAR2 NCAR10
[[278  26 109  29  34  11]
 [ 22 219  80  16  99  15]
 [ 62  85 183  11  70  13]
 [ 31  29   8 251 157  18]
 [  5   5  22  15 464  13]
 [ 10   7   6   7  16 474]]

HAR2 NAR5
[[304  71  78   0  43   0]
 [  0 237  59   0 145   0]
 [ 36  78 170   3 116 154]
 [ 73   0  15 270 133   0]
 [ 16   8   9  40 459   0]
 [  0   0   0   0   0 383]]

HAR2 NAR10
[[251  24 145  58  18   0]
 [  4 247 146   0  44   0]
 [ 53 105 245  10   5 295]
 [ 45   9   2 292 143   0]
 [ 15  25  22   6 464   0]
 [  0   0  12   0   0 215]]

HAR2 NNAR5
[[265 152   0  62  17   0]
 [  4 341   0   1  95   0]
 [ 45 274   0  17  67 148]
 [ 30   0   0 345 116   0]
 [  0  27   0  19 486   0]
 [  0   0   0   0   0 389]]

HAR2 NNAR10
[[251  42  42  59 102   0]
 [ 55 199   0   0 187   0]
 [ 96 102 262   0 117 121]
 [ 28   0   5 346 112   0]
 [ 31   0   2  12 487   0]
 [  0   0 149   0   0  93]]
