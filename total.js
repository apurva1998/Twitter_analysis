var MongoClient = require('mongodb').MongoClient;
	var url = "mongodb://localhost:27017/twitter";

	MongoClient.connect(url, function(err, db) {
		if (err) throw err;
			db.collection("merged").findOne({}, function(err, result) {
		if (err) throw err;
			var severe = result.class;
			if(severe=='M'){
			document.getElementById('severity').innerHTML=severe;
			}
			db.close();
	});
	});