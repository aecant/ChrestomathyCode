function all_elements_equal(array) {
    for (var elem of array) {
        if (elem !== array[0]) {
            return false;
        }
    }
    return true;
}

var int_args = process.argv.slice(2).map(num => parseInt(num, 10));
process.stdout.write(all_elements_equal(int_args) ? '_true_' : '_false_');