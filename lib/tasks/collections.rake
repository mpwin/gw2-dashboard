namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = [
      # Weapon

      # Heavy Armor
      { name: 'Chainmail',  skin_api_ids: [ 1,  2, 20, 26, 81, 2041], note: 'Loot' },
      { name: 'Scallywag',  skin_api_ids: [ 7,  8, 27],               note: 'Loot' },
      { name: 'Worn Chain', skin_api_ids: [14, 21],                   note: 'Loot' },
      { name: 'Worn Scale', skin_api_ids: [23, 24],                   note: 'Loot' },

      # Medium Armor
      { name: 'Rawhide',    skin_api_ids: [ 5,  6, 19], note: 'Loot' },
      { name: 'Sneakthief', skin_api_ids: [11, 12],     note: 'Loot' },
      { name: 'Studded',    skin_api_ids: [17, 22],     note: 'Legacy Armor Reward Track' },
      { name: 'Swindler',   skin_api_ids: [28, 31],     note: 'Loot' },

      # Light Armor
      { name: 'Apprentice', skin_api_ids: [ 3,  4, 16, 25, 29], note: 'Loot' },
      { name: 'Country',    skin_api_ids: [13, 18],             note: 'Loot' },
      { name: 'Seer',       skin_api_ids: [ 9, 10, 30],         note: 'Loot' }
    ]

    collection_data.each do |data|
      collection = Collection.find_or_initialize_by(name: data[:name])

      collection.skins = Skin.where(api_id: data[:skin_api_ids])
      collection.note  = data[:note]

      puts collection.name
      collection.save!
    end
  end
end
