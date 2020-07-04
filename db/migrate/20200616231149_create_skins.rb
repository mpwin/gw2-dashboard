class CreateSkins < ActiveRecord::Migration[6.0]
  def change
    create_table :skins do |t|
      t.integer :api_id
      t.string  :name
      t.string  :category
      t.text    :flags
      t.text    :restrictions
      t.string  :icon
      t.string  :rarity
      t.text    :description
      t.string  :bracket
      t.string  :weight_class

      t.timestamps
    end
  end
end
