#find out why Apache is returning a 500 error.
sudo strace -f -e trace=file -p $(pgrep apache2 | head -n 1)
