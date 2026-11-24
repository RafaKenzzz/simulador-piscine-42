mkdir test0 test2
printf '1234' > test1
printf '1' > test3
printf '12' > test4
ln test3 test5
ln -s test0 test6
chmod 715 test0
chmod 714 test1
chmod 504 test2
chmod 404 test3
chmod 641 test4
chmod -h 755 test6
touch -t 06012047 test0
touch -t 06012146 test1
touch -t 06012245 test2
touch -t 06012344 test3
touch -t 06012343 test4
touch -h -t 06012220 test6
ls -l
tar -cf exo2.tar *
