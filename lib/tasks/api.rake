namespace :api do
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
