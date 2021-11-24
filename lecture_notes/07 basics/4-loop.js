function sum(...args){
    let output = 0;
    for(const number of args){
        output += number;
    }
    return output;
}

console.log(sum(5,3,2));