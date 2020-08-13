require 'rails_helper'

RSpec.describe Collection, type: :model do
  describe 'associations' do
    it { should have_many(:skins) }
  end

  describe 'validations' do
    it { should validate_presence_of(:name) }
    it { should validate_presence_of(:category) }
  end

  it 'sets its category on skin association' do
    collection = Collection.new
    skin       = Skin.new(category: 'Weapon')

    collection.skins << skin

    expect(collection.category).to eq('Weapon')
  end
end
