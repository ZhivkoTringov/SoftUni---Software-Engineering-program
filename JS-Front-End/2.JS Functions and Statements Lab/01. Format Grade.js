function formatGrade(grade) {
    gradeDesc = ''
    if (grade < 3) {
        gradeDesc = `Fail (${2})`
    } else if (grade < 3.5) {
        gradeDesc = 'Poor'
    } else if (grade < 4.5) {
        gradeDesc = 'Good'
    } else if (grade < 5.5) {
        gradeDesc = 'Very good'
    } else if (grade >= 5.5) {
        gradeDesc = 'Excellent'
    }

    if (grade < 3) {
        console.log(gradeDesc);
    } else {
        console.log(`${gradeDesc} (${grade.toFixed(2)})`);
    }
}
