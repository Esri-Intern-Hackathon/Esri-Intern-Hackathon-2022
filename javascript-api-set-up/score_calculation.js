function averageBaseScore(walkabilityScore, bikeScore, transitScore, driveScore) {
    sumOfAllScores = walkabilityScore + bikeScore + transitScore + driveScore
    averageOfAllScores = sumOfAllScores/4
    return averageOfAllScores 
}


function weightedSumScore(userWalkWeight, userBikeWeight, userTransitWeight, userDriveWeight, defaultWalkScore, defaultBikeScore, defaultTransitScore, defaultDriveScore) {
// you'll have 10 integers

    weightedSum = userWalkWeight * defaultWalkScore + userBikeWeight * defaultBikeScore + userTransitWeight * defaultTransitScore + userDriveWeight * defaultDriveScore
    normalizedScore = weightedSum * 0.1
    return normalizedScore

}



// console.log(averageBaseScore(70, 90, 50, 90, 50))
console.log(weightedSumScore(1, 2, 4, 1, 2, 70, 87, 98, 76, 39))