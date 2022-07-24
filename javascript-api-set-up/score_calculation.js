function averageBaseScore(walkabilityScore, bikeScore, transitScore, scootScore, driveScore) {
    sumOfAllScores = walkabilityScore + bikeScore + transitScore + scootScore + driveScore
    averageOfAllScores = sumOfAllScores/5
    return averageOfAllScores 
}


function getDefaultScores() {

}


function getNormalizedWeights() {

}

function getDefaultScores() {
    var defaultScores = [];
    defaultScores.push();
    return defaultScores

}

function weightedSumScore(userWalkWeight, userBikeWeight, userTransitWeight, userScootWeight, userDriveWeight, defaultWalkScore, defaultBikeScore, defaultTransitScore, defaultScootScore, defaultDriveScore) {
// you'll have 10 integers

    weightedSum = userWalkWeight * defaultWalkScore + userBikeWeight * defaultBikeScore + userTransitWeight * defaultTransitScore + userScootWeight * defaultScootScore + userDriveWeight * defaultDriveScore
    return weightedSum

}



console.log(averageBaseScore(70, 90, 50, 90, 50))