
/**
 * Creates a function that returns "Hello World".
 *
 * @return {function} A function that takes any number of arguments and returns "Hello World".
 */
const createHelloWorld = function () {
    return function (...args) {
        return "Hello World";
    }
}

const f = createHelloWorld();
console.log(f());