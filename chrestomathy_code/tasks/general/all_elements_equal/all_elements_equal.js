function all_elements_equal(array) {
    return array.every((elem) => elem === array[0]);
}

var int_args = process.argv.slice(2).map(Number);
console.log(all_elements_equal(int_args) ? "_true_" : "_false_");
