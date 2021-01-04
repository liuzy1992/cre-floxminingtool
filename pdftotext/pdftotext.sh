#!/usr/bin/env bash
# vim: set noexpandtab tabstop=2:

declare -g -A __sourced__files__
if [[ ! -v __sourced__files__[$BASH_SOURCE] || $__force__source__ ]]; then
	__sourced__files__[$BASH_SOURCE]=$(realpath "$BASH_SOURCE")
	function pdftotext {
		declare exec_opt
		while true; do
			case $1 in
				-h|--help)
#					enable cat
					cat "${__sourced__files__[$BASH_SOURCE]%.sh}_help.txt"
					return
					;;
				--exec)
					exec_opt=exec
					shift
					;;
				--)
					shift
					break
					;;
				-*)
					echo "$FUNCNAME:ERROR:Bad option '$1'." >&2
				 	return -1
					;;
				*)
					break
					;;
			esac
		done

		declare f=$1
		$exec_opt pdftotext -nodiag -nopgbrk "$f" -
	}

	if ! { ( return ) } 2>/dev/null; then
		set -e
		pdftotext --exec "$@" || exit
	fi
fi

