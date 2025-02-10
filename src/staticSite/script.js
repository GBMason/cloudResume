let fetchRes = fetch(
	"https://40b4sc3ead.execute-api.us-east-1.amazonaws.com/Prod/viewcount");
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d.N)
				let htmlSegment = 
					"<h2>Thanks for visiting! You are the " + d.N + " person to view this page.</h2>";
					document.getElementById("views").innerHTML = htmlSegment
			}
		)