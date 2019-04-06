#!/bin/bash
timestamp=$(date)
BASHDIR=$(pwd)

#change dir for testing
pushd /mnt/c/Users/corey/Corey-All-

for repository in $(dirname $(find . -name "*.git" ! -path "./gitBackup/*")); do

    #PROMPT
    echo ==============================
    echo STATUS for ${repository}
    echo ==============================

    git -C ${repository} status

    read command
    while [[ ! "${command}" == "" ]]; do

        #PROMPT
        echo ==============================
        echo STATUS for ${repository}
        echo ==============================

        #statements
        #git -C ${repository} $(echo ${command})
        echo ${repository}
        echo ${command}

        read command
    done
done

echo DONE
echo ${timestamp}

#return to bash directory
popd

#add variables that need to be unset
unset dir timestamp command

