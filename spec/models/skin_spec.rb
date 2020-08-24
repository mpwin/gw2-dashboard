require 'rails_helper'

RSpec.describe Skin, type: :model do
  it { should serialize(:flags) }
  it { should serialize(:restrictions) }

  describe 'associations' do
    it { should belong_to(:collection).optional }

    it 'updates its collection when its unlocked field is changed' do
      skin = Skin.create(api_id: 1, unlocked: false)
      skin.create_collection
      expect(skin.collection.unlocked).to eq(false)

      skin.update(unlocked: true)
      expect(skin.collection.unlocked).to eq(true)
    end
  end

  describe 'validations' do
    it { should validate_presence_of(:api_id) }
  end
end
