#!bin\bash
timeStamp=$(date)
printf "%s\n%s\n\n" "$USER" "$timeStamp" > R3dHand/gitLog

attempts=0
results=()
gitdirs=$(find . -name ".git")
for i in $(printf "$gitdirs"); do
	printf "====================${i::-5}\n\n" >> R3dHand/gitLog
	dir=${i::-5} 
	status=$(git -C $dir status)
	printf "%s" "$status"
	printf "\n\n====================DONE\n\n" >> R3dHand/gitLog
	if [[ "$status" =~ "Changes not staged" ]]; then
		printf "\n\nADD TO %s...(y/n)\n" "${i::-5}"

		read inputAdd
		if [[ "$inputAdd" =~ "y" ]] || [[ "$input" =~ "Y" ]]; then
			git -C $dir add .
			git -C $dir status
			newStatus=$(git -C $dir status)
		fi	

		if [[ "$newStatus" =~ "Changes to be committed:" ]]; then
			printf "\n\nCOMMIT TO %s...(y/n)\n" "${i::-5}"

			read inputCommit
			if [[ "$inputCommit" =~ "y" ]] || [[ "$input" =~ "Y" ]]; then
			git -C $dir commit --amend --no-edit
			git -C $dir status
			else
				continue
			fi
		fi	
	fi



done
