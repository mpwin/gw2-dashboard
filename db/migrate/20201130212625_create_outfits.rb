class CreateOutfits < ActiveRecord::Migration[6.0]
  def change
    create_table :outfits do |t|
      t.integer :api_id
      t.string  :name
      t.string  :icon
      t.boolean :unlocked, default: false
    end
  end
end
