---
layout: post
title: "python profiling md5 vs sha1"
author: "jungjik.lee"
categories: article
tags: [python, hash, profiling]
---

# :snake: python profiler
- python profiler : [https://docs.python.org/ko/3/library/profile.html](https://docs.python.org/ko/3/library/profile.html)
- profiling code
<pre><code>
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()

pr.enable()
# ... do something ...
pr.disable()

s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
</code></pre>

# :watch: md5 vs sha1 and sha256
- md5 hash code
<pre><code>
In [8]: import hashlib
In [9]: with open(file, 'rb') as f:
   ...:     hash = hashlib.md5(f.read()).hexdigest()
   ...:     print(hash)
   ...: 
682832d0f3cbd52eb8ad5f6ef83f7e04
</code></pre>

- hash result with profiling code
  - i7 ivy bridge cpu, ssd, 2.5MB 사이즈의 이미지 파일(x1000번) 프로파일링 해본 결과이다.
  - 당연한 거겠지만, md5 와 sha1과는 별 차이가 없고 sha256는 2배 정도 차이가 난다.
  - 일반적으로 파일이 같은걸 확인하려면 sha1 정도면 괜찮을 듯 하다.
<pre><code>
      6001 function calls in 4.573 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.139    0.000    4.573    0.005 test.py:7(get_md5)
1000    3.497    0.003    3.497    0.003 {built-in method _hashlib.openssl_md5}
1000    0.809    0.001    0.809    0.001 {method 'read' of '_io.BufferedReader' objects}
1000    0.088    0.000    0.088    0.000 {built-in method io.open}
1000    0.035    0.000    0.035    0.000 {method '__exit__' of '_io._IOBase' objects}
1000    0.004    0.000    0.004    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

      6001 function calls in 4.227 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.135    0.000    4.227    0.004 test.py:11(get_sha1)
1000    3.166    0.003    3.166    0.003 {built-in method _hashlib.openssl_sha1}
1000    0.802    0.001    0.802    0.001 {method 'read' of '_io.BufferedReader' objects}
1000    0.087    0.000    0.087    0.000 {built-in method io.open}
1000    0.034    0.000    0.034    0.000 {method '__exit__' of '_io._IOBase' objects}
1000    0.005    0.000    0.005    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

      6001 function calls in 8.106 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.136    0.000    8.106    0.008 test.py:15(get_sha256)
1000    7.026    0.007    7.026    0.007 {built-in method _hashlib.openssl_sha256}
1000    0.815    0.001    0.815    0.001 {method 'read' of '_io.BufferedReader' objects}
1000    0.088    0.000    0.088    0.000 {built-in method io.open}
1000    0.035    0.000    0.035    0.000 {method '__exit__' of '_io._IOBase' objects}
1000    0.005    0.000    0.005    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
</code></pre>

- 동영상(60MB) hash 만드는데 걸리는 시간, md5(0.311s), sha1(0.112s), sha256(0.210s)
- md5의 경우엔 _hashlib.openssl_md5 에서 시간을 좀 쓰다.
- 가성비로는 sha1가 제일 좋을 듯 싶다.
<pre><code>
      7 function calls in 0.311 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1    0.003    0.003    0.311    0.311 test.py:7(get_md5)
      1    0.219    0.219    0.219    0.219 {method 'read' of '_io.BufferedReader' objects}
      1    0.089    0.089    0.089    0.089 {built-in method _hashlib.openssl_md5}
      1    0.000    0.000    0.000    0.000 {built-in method io.open}
      1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
      1    0.000    0.000    0.000    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

      7 function calls in 0.112 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1    0.004    0.004    0.112    0.112 test.py:11(get_sha1)
      1    0.083    0.083    0.083    0.083 {built-in method _hashlib.openssl_sha1}
      1    0.025    0.025    0.025    0.025 {method 'read' of '_io.BufferedReader' objects}
      1    0.000    0.000    0.000    0.000 {built-in method io.open}
      1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
      1    0.000    0.000    0.000    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

      7 function calls in 0.210 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1    0.003    0.003    0.210    0.210 test.py:15(get_sha256)
      1    0.181    0.181    0.181    0.181 {built-in method _hashlib.openssl_sha256}
      1    0.026    0.026    0.026    0.026 {method 'read' of '_io.BufferedReader' objects}
      1    0.000    0.000    0.000    0.000 {built-in method io.open}
      1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
      1    0.000    0.000    0.000    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
</code></pre>
