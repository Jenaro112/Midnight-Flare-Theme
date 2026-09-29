import fs from "fs";

const MAX_RETRIES = 5;
let currentAttempt = 0;

/**
 * Calculates the total sum.
 */
function calculateSum(a, b) {
    const result = a + b;
    if (result > 10) {
        return "Too big!";
    }
    return result;
}

class UserProfile {
    constructor(name) {
        this.name = name;
        this.isActive = true;
    }

    printGreeting() {
        console.log(`Hello, ${this.name}!`);
    }
}

export default calculateSum;
