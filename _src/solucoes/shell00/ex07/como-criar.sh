patch -o b a < sw.diff
diff a b > teste.diff
diff teste.diff sw.diff && echo "b está certo"
