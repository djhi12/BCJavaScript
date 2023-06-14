--[[
In Roblox Studio, "Teams" refers to a feature that allows you to organize players into different groups or factions within a game. Teams can be useful for various purposes, such as creating team-based gameplay, distinguishing different roles or affiliations, or organizing players for specific objectives or competitions.

Teams in Roblox Studio are represented by the Teams service, which provides a set of functions and properties to manage and manipulate teams. Here are some common operations you can perform with teams in Roblox Studio:

Creating Teams: You can create teams using the TeamsService object. Teams are usually created before the game starts or when a new round begins. Each team is identified by a unique numerical TeamId value.

Adding Players to Teams: You can assign players to teams using the TeamsService:SetPlayerTeam() function. By specifying the player's UserId and the desired TeamId, you can move players between teams during gameplay or assign them to teams when they join the game.

Accessing Team Data: The TeamsService provides functions to access team-specific data, such as retrieving a team's name, color, or players. For example, you can use the TeamsService:GetTeamName() function to get the name of a specific team.

Balancing Teams: If you want to ensure fair gameplay, you can implement a team-balancing system by checking the number of players on each team and automatically transferring players to different teams to even out the player count.

Customizing Team Properties: You can modify various properties of teams, such as their name, team color, and team spawn location. These settings can help differentiate teams visually and functionally within the game.

By using teams in Roblox Studio, you can create dynamic and engaging gameplay experiences that involve cooperation, competition, and teamwork. The specific implementation of teams will depend on the game you are creating and your desired gameplay mechanics.

--]] 


-- Example Program
-- Get the Teams service
local teamsService = game:GetService("Teams")

-- Create teams
local team1 = Instance.new("Team")
team1.Name = "Red Team"
team1.TeamColor = BrickColor.new("Bright red")
team1.Parent = teamsService

local team2 = Instance.new("Team")
team2.Name = "Blue Team"
team2.TeamColor = BrickColor.new("Bright blue")
team2.Parent = teamsService

-- Function to assign players to teams
local function assignPlayerToTeam(player, team)
    -- Check if the player and team exist
    if player and player:IsA("Player") and team and team:IsA("Team") then
        -- Set the player's team
        player.Team = team
    end
end

-- Example usage:
game.Players.PlayerAdded:Connect(function(player)
    -- Assign new players to teams
    if player.Name == "Player1" then
        assignPlayerToTeam(player, team1)
    elseif player.Name == "Player2" then
        assignPlayerToTeam(player, team2)
    end
end)

-- Custom function to balance teams
local function balanceTeams()
    local redTeamPlayerCount = #team1:GetPlayers()
    local blueTeamPlayerCount = #team2:GetPlayers()

    if redTeamPlayerCount > blueTeamPlayerCount + 1 then
        -- Move a player from red team to blue team
        local playerToMove = team1:GetPlayers()[1]
        assignPlayerToTeam(playerToMove, team2)
    elseif blueTeamPlayerCount > redTeamPlayerCount + 1 then
        -- Move a player from blue team to red team
        local playerToMove = team2:GetPlayers()[1]
        assignPlayerToTeam(playerToMove, team1)
    end
end

-- Example usage:
game.Players.PlayerRemoving:Connect(function(player)
    -- Rebalance teams when a player leaves
    balanceTeams()
end)

--[[
In this example, we start by creating two teams: a red team and a blue team. We set their names and team colors using the Team object's properties and then assign them to the Teams service.

Next, we define the assignPlayerToTeam function, which takes a player and a team as parameters and assigns the player to the specified team by setting the player's Team property.

We then use the PlayerAdded event to assign new players to teams based on their names. In this case, if the player's name is "Player1," they are assigned to the red team, and if their name is "Player2," they are assigned to the blue team.

Additionally, we define the balanceTeams function, which checks the player counts on both teams and balances them if one team has more players than the other by more than one player. This function is called whenever a player leaves the game, using the PlayerRemoving event.

This is just a basic example to showcase the usage of teams in Roblox Studio. You can expand upon this code and customize it according to your specific game requirements and logic.    
--]]