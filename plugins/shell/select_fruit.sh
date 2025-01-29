FRUIT=$1
if [ $FRUIT = APPLE ]; then
    echo "You selected apple"
elif [ $FRUIT = ORANGE ]; then
    echo "You selected orange"
elif [ $FRUIT = GRAPE ]; then
    echo "You selected grape"
else
    echo "You selected other fruit"
fi