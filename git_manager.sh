#!/bin/bash
timestamp=$(date)
BASHDIR=$(pwd)

#change dir for testing
cd /mnt/c/Users/corey/Corey-All-/R3dHand

for repository in $(dirname $(find . -name "*.git" ! -path "./gitBackup/*")); do

    pushd ${repository}
    #PROMPT
    echo ==============================
    echo STATUS for ${repository}
    echo ==============================

    git status

    read command
    while [[ ! "${command}" == "" ]]; do
        #statements
        cmd.exe /c git $(echo ${command})

        echo ==============================
        echo STATUS for ${repository}
        echo ==============================

        git status

        read command
    done
    popd
done

echo DONE
echo ${timestamp}

#return to bash directory
cd ${BASHDIR}

#add variables that need to be unset
unset dir timestamp command

