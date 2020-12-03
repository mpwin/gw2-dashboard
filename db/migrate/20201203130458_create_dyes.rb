class CreateDyes < ActiveRecord::Migration[6.0]
  def change
    create_table :dyes do |t|
      t.integer :api_id
      t.string  :name
      t.text    :base_rgb
      t.string  :hue
      t.string  :material
      t.string  :rarity
      t.boolean :unlocked, default: false
    end
  end
end
