function inventory(input){
    let heroes = [];

    for (const line of input) {
        let [hero, level, items] = line.split(' / ');
        level = Number(level);
        heroes.push({hero, level, items});
    }
    
    let sortedHeroes = heroes.sort((heroA, heroB) => heroA.level - heroB.level);
    for (const {hero, level, items} of sortedHeroes) {
        console.log(`Hero: ${hero}`);
        console.log(`level => ${level}`);
        console.log(`items => ${items}`);
    }
}