function solve(input){
    class Song {
        constructor(type, name, time){
            this.type = type;
            this.name = name;
            this.time = time;
        }

    }

    let songs = [];
    let numberOfSong = input.shift();
    let typeOfSong = input.pop();

    for (let i = 0; i < numberOfSong; i++) {
        let [type, name, time] = input[i].split('_');
        let song = new Song(type, name, time);
        songs.push(song);
    }

    if (typeOfSong === 'all') {
        songs.forEach((i) => console.log(i.name));
    } else {
        let filtered = songs.filter((i) => i.type === typeOfSong);
        filtered.forEach((i) => console.log(i.name));
    }
}
