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
#shopt -s inherit_errexit        # make subshells inherit errexit behavior

IFS=$'\n\t' # set array separator to newline and tab to avoid word splitting bugs
SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
ROOT_PID=$$

/usr/bin/ssh "$1" 'cd "'"$2"'" && /usr/local/bin/tsunami connect '"$3"' get '"$4"' exit'

###
function finally {
      # Tidy up
        echo > /dev/null
    }
trap finally EXIT
echo "return 0" > /dev/null # Make sure the exit code of the script is 0
