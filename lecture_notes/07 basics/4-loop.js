function sum(...args){
    let output = 0;
    for(const number of args){
        output += number;
    }
    return output;
}

const result = sum(5,3,2)
console.log(result);
