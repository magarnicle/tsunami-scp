#!/bin/bash
### Bash Environment Setup
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
# https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
set -o xtrace                 # print every command before executing (for debugging)
set -o nounset                  # make using undefined variables throw an error
set -o errexit                  # exit immediately if any command returns non-0
set -o pipefail                 # exit from pipe if any command within fails
set -o errtrace                 # subshells should inherit error handlers/traps
shopt -s dotglob                # make * globs also match .hidden files
shopt -s inherit_errexit        # make subshells inherit errexit behavior

IFS=$'\n\t' # set array separator to newline and tab to avoid word splitting bugs
SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
ROOT_PID=$$

local server="$2"
local port="$3"
shift 2
args="$#"
local destination="${args[-1]}"
mkdir -p $(dirname "$local")
local sources=(( ${#@} - 1))
for (( i=0; i<$sources ; i+=1 )) ; do
    transfers="$transfers get ${args[i] $fname"
done
tsunami connect $server $port $transfers close quit

###
function finally {
      # Tidy up
  }
trap finally EXIT
echo "return 0" > /dev/null # Make sure the exit code of the script is 0 on success
