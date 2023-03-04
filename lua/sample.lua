local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"--leaderstats should be mentioned like this only, otherwise the leaderboard will not pop up
	
	--parent the leaderstats folder so that every player will have their own folder called leaderstats
	leaderstats.Parent = player
	
	--create a variable for the currency
	local bucks = Instance.new("IntValue") --IntValue means integer value since currency will be in the form of numbers
	bucks.Name = "Bucks"
	bucks.Value = 0 							--Initally the value will be 0
	bucks.Parent = leaderstats

    