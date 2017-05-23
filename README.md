python 脚本
命令行获取某文件 hash 值, 包括 MD5、SHA-1、SHA-256、SHA-512

调用方法方法
```
python check_hash.py [FILE]
```

结果打印 hash 值列表, 供与官方提供值进行比对。
e.g.
```
method || value
------------------------------------------------
md5    || 259b9e54bbc9920bfc6712607176dc54
sha1   || da39a3ee5e6b4b0d3255bfef95601890afd80709
sha256 || e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
sha512 || cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
```

文件不存在时
```
[FILE] is docopt. is an invalid file path
```
