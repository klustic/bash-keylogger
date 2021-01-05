debug_trap () {
  curl -F cmd=`echo "[$(hostname -f)] $BASH_COMMAND" | base64 -w0` http://127.0.0.1:8000/logs &>/dev/null
}
trap debug_trap DEBUG
