require 'rails_helper'

RSpec.describe Collection, type: :model do
  describe 'associations' do
    it { should have_many(:skins) }

    it 'raises an error when adding a skin of a different category' do
      collection = Collection.new(category: 'Weapon')
      skin       = Skin.new(category: 'Armor')
  
      expect { collection.skins << skin }.to raise_error("Category mismatch")
    end

    it 'raises an error when adding a skin of a different weight class' do
      collection = Collection.new(category: 'Armor', weight_class: 'Heavy')
      skin       = Skin.new(category: 'Armor', weight_class: 'Light')

      expect { collection.skins << skin }.to raise_error("Weight class mismatch")
    end
  end

  describe 'validations' do
    it { should validate_presence_of(:name) }
    it { should validate_presence_of(:category) }
  end

  it 'sets its category field on initial skin association' do
    collection = Collection.new
    skin       = Skin.new(category: 'Weapon')

    collection.skins << skin

    expect(collection.category).to eq('Weapon')
  end

  it 'sets its weight class field on initial skin association' do
    collection = Collection.new
    skin       = Skin.new(category: 'Armor', weight_class: 'Heavy')

    collection.skins << skin

    expect(collection.weight_class).to eq('Heavy')
  end

  it 'updates its unlocked field after adding a skin' do
    collection = Collection.new
    skin       = Skin.new(unlocked: true)

    collection.skins << skin

    expect(collection.unlocked).to eq(true)
  end
end
