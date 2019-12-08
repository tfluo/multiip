for LINE in `cat $1`
do
  ip -4 addr add "$LINE" dev ens33
done

for LINEin `cat $2`
do
  ip -6 addr add "$LINE" dev ens33
done
