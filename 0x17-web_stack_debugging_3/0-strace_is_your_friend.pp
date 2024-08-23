sudo strace -f -e trace=file -p $(pgrep apache2 | head -n 1)
