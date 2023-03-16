function towns (input){
    let info = {
        'town': '',
        'latitude': '',
        'longitude' : ''
    };
    
    for (const data of input) {
        let [town, latitude, longitude] = data.split(' | ')
        info['town'] = town;
        info['latitude'] = Number(latitude).toFixed(2);
        info['longitude'] = Number(longitude).toFixed(2);


        console.log(`{ town: '${info['town']}', latitude: '${info['latitude']}', longitude: '${info['longitude']}' }`);
    }

}