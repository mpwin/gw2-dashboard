namespace :api do
  namespace :dyes do
    desc 'Create and update dyes'
    task get: :environment do
      uri      = URI::HTTPS.build(host: 'api.guildwars2.com', path: '/v2/colors')
      response = Net::HTTP.get(uri)

      JSON.parse(response).each_slice(200) do |ids|
        uri.query = { ids: ids.join(',') }.to_query
        response  = Net::HTTP.get(uri)

        JSON.parse(response).each do |obj|
          dye = Dye.find_or_initialize_by(api_id: obj['id'])

          dye.name     = obj['name']
          dye.base_rgb = obj['base_rgb']
          dye.hue      = obj['categories'][0]
          dye.material = obj['categories'][1]
          dye.rarity   = obj['categories'][2]

          if dye.new_record?
            puts "CREATE -- #{dye.api_id}, #{dye.name}"
          elsif dye.changed?
            puts "UPDATE -- #{dye.api_id}, #{dye.name} -- #{dye.changed_attributes}"
          else
            puts "Exists -- #{dye.api_id}, #{dye.name}"
          end

          dye.save!
        end

        sleep(2)
      end
    end
  end

  namespace :outfits do
    desc 'Create and update outfits'
    task get: :environment do
      uri      = URI::HTTPS.build(host: 'api.guildwars2.com', path: '/v2/outfits')
      response = Net::HTTP.get(uri)

      JSON.parse(response).each_slice(200) do |ids|
        uri.query = { ids: ids.join(',') }.to_query
        response  = Net::HTTP.get(uri)

        JSON.parse(response).each do |obj|
          outfit = Outfit.find_or_initialize_by(api_id: obj['id'])

          outfit.name = obj['name']
          outfit.icon = obj['icon']

          if outfit.new_record?
            puts "CREATE -- #{outfit.api_id}, #{outfit.name}"
          elsif outfit.changed?
            puts "UPDATE -- #{outfit.api_id}, #{outfit.name} -- #{outfit.changed_attributes}"
          else
            puts "Exists -- #{outfit.api_id}, #{outfit.name}"
          end

          outfit.save!
        end

        sleep(2)
      end
    end
  end

  namespace :skins do
    desc 'Create and update skins'
    task get: :environment do
      uri      = URI::HTTPS.build(host: 'api.guildwars2.com', path: '/v2/skins')
      response = Net::HTTP.get(uri)

      JSON.parse(response).each_slice(200) do |ids|
        uri.query = { ids: ids.join(',') }.to_query
        response  = Net::HTTP.get(uri)

        JSON.parse(response).each do |obj|
          skin = Skin.find_or_initialize_by(api_id: obj['id'])

          skin.name         = obj['name']
          skin.category     = obj['type']
          skin.flags        = obj['flags']
          skin.restrictions = obj['restrictions']
          skin.icon         = obj['icon']
          skin.rarity       = obj['rarity']
          skin.description  = obj['description']

          if obj.has_key?('details')
            skin.bracket      = obj['details']['type']
            skin.weight_class = obj['details']['weight_class']  
          end

          if skin.new_record?
            puts "CREATE -- #{skin.api_id}, #{skin.name}"
          elsif skin.changed?
            puts "UPDATE -- #{skin.api_id}, #{skin.name} -- #{skin.changed_attributes}"
          else
            puts "Exists -- #{skin.api_id}, #{skin.name}"
          end

          skin.save!
        end

        sleep(2)
      end
    end
  end
end
