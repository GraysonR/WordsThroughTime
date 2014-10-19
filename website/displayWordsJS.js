var words = [12,44,56,85,1,9,4,2,44,18,24,2,789,465,45,456,87,13,54,4,4,8846,4,562,48,648,1,1,1,1,1,2,8,5,9,78,7,8,7,47,98,878,7,12,8,8];
var sorted = new Array();
var count = 0;

function swap(array, i1, i2) {

	var temp = array[i1];
	array[i1] = array[i2];
	array[i2] =temp;
}

function sort(word) {

	var len = word.length;
	var i;
	var j;
	var stop;

	for(i = 0; i < len; i++) {
		for(j = 0; j <= len-i; j++) {
			if(word[j] < word[j + 1]) {
				swap(word, j, j+1);
			}
		}
	}

	print(word);

	return word;
}

function top25(word, done) {
	var i = 0;
	while(i != 25) {
		done[i] = word[i];
		i++;
	}
	print(done);
	return done;
}

function main() {
	var array = sort(words);
	top25(array, sorted);
}


main();