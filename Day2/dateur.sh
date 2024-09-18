YEAR=$1

rm -rf $YEAR
mkdir $YEAR

for MONTH in $(seq -f "%02g" 1 12); do
    MONTH_NAME=$(date -d "$YEAR-$MONTH-01" +%b)
    mkdir $YEAR/$MONTH-$MONTH_NAME
    DAYS_IN_MONTH=$(date -d "$YEAR-$MONTH-01 + 1 month - 1 day" +%d)
    for DAY in $(seq -f "%02g" 1 $DAYS_IN_MONTH); do
        DAY_OF_WEEK=$(date -d "$YEAR-$MONTH-$DAY" +%A)
        echo "$YEAR/$MONTH/$DAY is a $DAY_OF_WEEK" > $YEAR/$MONTH-$MONTH_NAME/$DAY.txt
    done
done




# MOIS=("01Janvier"  "02Février"  "03Mars"  "04Avril"  "05Mai"  "06Juin"  "07Juillet"  "08Août"  "09Septembre"  "10Octobre"  "11Novembre"  "12Décembre")

# for I in ${MOIS[@]}; do
#     mkdir ./$1/$I
# done
