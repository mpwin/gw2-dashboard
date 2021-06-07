namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = YAML.load_file("#{Rails.root}/lib/collections.yml")

    puts 'WEAPON'
    collection_data['weapons'].each do |data|
      save_collection(data, 'Weapon')
    end

    puts 'HEAVY ARMOR'
    collection_data['heavy_armor'].each do |data|
      save_collection(data, 'Armor', 'Heavy')
    end

    puts 'MEDIUM ARMOR'
    collection_data['medium_armor'].each do |data|
      save_collection(data, 'Armor', 'Medium')
    end

    puts 'LIGHT ARMOR'
    collection_data['light_armor'].each do |data|
      save_collection(data, 'Armor', 'Light')
    end

    handle_special_cases(collection_data['special_cases'])
  end
end

def save_collection(data, category, weight_class = nil)
  collection = Collection.find_or_initialize_by(
    name:         data['name'],
    category:     category,
    weight_class: weight_class
  )

  collection.skins = Skin.where(category: category)
                         .where(weight_class: weight_class)
                         .where('name LIKE ?', data['name'] + ' %')

  collection.note  = data['note']

  puts '  ' + collection.name
  collection.save!
end

def handle_special_cases(cases)
  puts 'SPECIAL CASES'

  cases['add_to_collection'].each do |data|
    skin = Skin.find_by(
      name:         data['skin'],
      category:     data['category'],
      weight_class: data['weight_class']
    )
    collection = Collection.find_by(
      name:         data['collection'],
      category:     data['category'],
      weight_class: data['weight_class']
    )

    puts "  Adding #{skin.name} to #{collection.name}"
    skin.collection = collection
    skin.save!
  end

  cases['remove_from_collection'].each do |data|
    skin = Skin.find_by(
      name:         data['skin'],
      category:     data['category'],
      weight_class: data['weight_class']
    )

    puts "  Removing #{skin.name} from #{skin.collection.name}"
    skin.collection = nil
    skin.save!
  end
end
