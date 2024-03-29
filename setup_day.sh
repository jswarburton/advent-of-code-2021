set -euo pipefail

if [ "$#" -ne 1 ]
then
  echo "One argument required"
  echo "Usage: ./setup_day.sh <DAY_NUMBER>"
  exit 1
fi

day=$1

echo "Creating files for day $day"

padded_day=$(printf "%02d" ${day})

sed -e "s/{{PADDED_DAY}}/${padded_day}/g" template/main_template.txt > main/day_"${padded_day}".py

sed -e "s/{{PADDED_DAY}}/${padded_day}/g" template/test_template.txt > tests/day_"${padded_day}"_test.py

session=$(<.session)
curl --cookie "session=${session}" https://adventofcode.com/2021/day/${day}/input -o main/resources/day${padded_day}-01.txt

echo "Successfully created files"
