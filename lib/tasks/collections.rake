namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = [
      # Weapon

      # Heavy Armor
      { name: 'Chainmail',        skin_api_ids: [ 1,  2, 20, 26, 81, 2041], note: 'Loot' },
      { name: 'Reinforced Scale', skin_api_ids: [41, 42, 72, 74, 77,  101], note: 'Loot' },
      { name: 'Scallywag',        skin_api_ids: [ 7,  8, 27, 33, 38,   92], note: 'Loot' },
      { name: 'Worn Chain',       skin_api_ids: [14, 21, 40, 50, 52,   96], note: 'Loot' },
      { name: 'Worn Scale',       skin_api_ids: [23, 24, 65, 66, 68,   99], note: 'Loot' },

      # Medium Armor
      { name: 'Rawhide',    skin_api_ids: [ 5,  6, 19, 32,   36,   89], note: 'Loot' },
      { name: 'Sneakthief', skin_api_ids: [11, 12, 35, 43,   47,   95], note: 'Loot' },
      { name: 'Studded',    skin_api_ids: [17, 22, 48, 59, 1719, 1783], note: 'Legacy Armor Reward Track' },
      { name: 'Swindler',   skin_api_ids: [28, 31, 60, 67,   71,   97], note: 'Loot' },

      # Light Armor
      { name: 'Apprentice', skin_api_ids: [ 3,  4, 16, 25, 29,  85], note: 'Loot' },
      { name: 'Country',    skin_api_ids: [13, 18, 53, 56, 64,  98], note: 'Loot' },
      { name: 'Magician',   skin_api_ids: [34, 37, 69, 70, 73, 100], note: 'Loot' },
      { name: 'Seer',       skin_api_ids: [ 9, 10, 30, 39, 45,  94], note: 'Loot' }
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
